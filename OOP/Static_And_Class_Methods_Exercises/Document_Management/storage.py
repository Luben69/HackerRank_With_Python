from Document_Management.category import Category
from Document_Management.topic import Topic
from Document_Management.document import Document


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def __edit_object(self, uid, collection, *args):
        obj = self.__get_object(uid, collection)
        if obj:
            obj.edit(*args)

    @staticmethod
    def __get_object(object, collection: list):
        return next((o for o in collection if o.id == object), None)

    def __delete_object(self, uid: int, collection: list):
        obj = self.__get_object(uid, collection)
        if obj:
            collection.remove(obj)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id):
        return self.__get_object(document_id, self.documents)

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])

