from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import response, status
from rest_framework.views import APIView
from iris_assignment_app.models import Iris
from iris_assignment_app.serializers import IrisSerializer
from rest_framework.permissions import IsAuthenticated

#Create your views here.
# class IrisListView(ListAPIView):
#     """GET - All the Iris list."""
#     permission_classes = [IsAuthenticated]
#     serializer_class = IrisSerializer
#     queryset = Iris.objects.all()

class IrisCreateView(GenericAPIView):
    """POST - Create Iris list"""
    permission_classes = [IsAuthenticated]
    serializer_class = IrisSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"success":"Data has been added."}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({"error":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        return response.Response({"unavailable":"Service is up..."}, status=status.HTTP_204_NO_CONTENT)

class IrisDeleteView(APIView):
    """DELETE - Delete Iris data by their id."""
    permission_classes = [IsAuthenticated]
    def delete(self,request, pk, format=None):
        iris = Iris.objects.filter(pk=pk)
        if len(iris)>0:
            iris = iris[0]
            iris.delete()
            return response.Response({"success":"Iris deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid iris id."}, status=status.HTTP_400_BAD_REQUEST)


# # Add from iris.data to the Iris database
# def add_iris_data():
#     with open('iris.data', 'r') as iris_file:
#         each_line = iris_file.readlines()
#         for each_l in each_line:
#             each_l_list = each_l.split(',')
#             try:
#                 sepal_length = each_l_list[0]
#                 sepal_width = each_l_list[1]
#                 petal_length = each_l_list[2]
#                 petal_width = each_l_list[3]
#                 iris_class = each_l_list[4]
#                 # Adding the data into database 
#                 iris = Iris()
#                 iris.sepal_length = sepal_length
#                 iris.sepal_width = sepal_width
#                 iris.petal_length = petal_length
#                 iris.petal_width = petal_width
#                 iris.iris_class = iris_class
#                 iris.save()
#             except:
#                 pass