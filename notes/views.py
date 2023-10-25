from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note


# Create your views here.


class NoteListView(ModelViewSet):
    queryset = Note.objects.all().order_by('-updated')
    serializer_class = NoteSerializer


# class NotesView(APIView):
#     def get(self, request):
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)



# @api_view(['GET'])
# def getNotes(request):
#     notes = Note.objects.all().order_by('-updated')
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def createNote(self, request):
#     serializer = NoteSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#
# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(body=data['body'])
#     serializer = NoteSerializer(note, many=False)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#
#
# @api_view(['PUT'])
# def updateNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted!')
