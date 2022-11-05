from rest_framework import serializers
from BookApp.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=('BookId','BookName','BookQuantity','BookGenre','BookBestSeller')