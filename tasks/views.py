from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet
from .serializers import TasksListSerializer
from .models import Task
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone

PAGINATION_NUMBER = 20
class TaskApi(ViewSet):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(operation_description=f"""provide auth token for user in the header of the request,
      get paginated tasks '{PAGINATION_NUMBER}' for authenticated user
    """)
    def tasks_list(self, request):
        try:
            tasks = Task.objects.filter(user_id=request.user.id).order_by("-created_at")
            paginator = PageNumberPagination()
            paginator.page_size = PAGINATION_NUMBER
            results = paginator.paginate_queryset(tasks, request)
            created_task = TasksListSerializer(results, many=True)
            return paginator.get_paginated_response(created_task.data)
        except:
            return Response({"server_error": "something wrong in server , please try later ."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(operation_description="provide auth token for user(engineer) in the header of the request")
    def mark_task_as_complete(self, request, task_id=None):
      try:
          task = Task.objects.get(id=task_id)
          if task.user_id == request.user.id:
              if not task.is_complete:
                if task.due_date < timezone.now():
                  task.type_of_task = "overdue"
                  task.save()
                else :
                  task.is_complete = True
                  task.type_of_task = "finished"
                  task.save()
                updated_task = TasksListSerializer(task)
                return Response({"task": updated_task.data},status=status.HTTP_200_OK)
              else : 
                return Response({"error", "task is already completed ."}, status=status.HTTP_400_BAD_REQUEST)
          else:
              return Response({"unauthorized", "you don't have permission ."}, status=status.HTTP_401_UNAUTHORIZED)
      except Task.DoesNotExist:
          return Response({"not_exist", "task is not exist ."}, status=status.HTTP_404_NOT_FOUND)
      except:
          return Response({"server_error": "something wrong in server , please try later ."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(operation_description=f"""provide auth token for user in the header of the request,
      get paginated completed tasks '{PAGINATION_NUMBER}' for authenticated user
    """)
    def tasks_finished_list(self, request):
        try:
            tasks = Task.objects.filter(
                user_id=request.user.id, is_complete=True).order_by("-created_at")
            paginator = PageNumberPagination()
            paginator.page_size = PAGINATION_NUMBER
            results = paginator.paginate_queryset(tasks, request)
            created_task = TasksListSerializer(results, many=True)
            return paginator.get_paginated_response(created_task.data)
        except:
            return Response({"server_error": "something wrong in server , please try later ."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(operation_description=f"""provide auth token for user in the header of the request,
      get paginated uncompleted tasks '{PAGINATION_NUMBER}' for authenticated user
    """)
    def tasks_unfinished_list(self, request):
        try:
            tasks = Task.objects.filter(
                user_id=request.user.id, is_complete=False).order_by("-created_at")
            paginator = PageNumberPagination()
            paginator.page_size = PAGINATION_NUMBER
            results = paginator.paginate_queryset(tasks, request)
            created_task = TasksListSerializer(results, many=True)
            return paginator.get_paginated_response(created_task.data)
        except:
            return Response({"server_error": "something wrong in server , please try later ."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)