from abc import ABC, abstractclassmethod
from typing import List
from langchain.docstore.document import Document

class AbstractVectorDataBase(ABC):

    @abstractclassmethod
    def update(cls, documents: List[Document]) -> None:
        """Updating DB with documents if they not already exist: Identification of documents via hash value in meta data """
        pass

    @abstractclassmethod
    def create(cls, name: str) -> None:
        """Create Vector Data Base """
        pass

    @abstractclassmethod
    def load_documents(cls, documents: List[Document]) -> None:
        """Loading documents into vector data base"""
        pass

    @abstractclassmethod
    def delete_documents(cls, documents: List[Document]) -> None:
        """Deleting documents from vector data base (if present in db): Identification of documents via hash value in meta data """
        pass

    @abstractclassmethod
    def delete(cls, name: str) -> None:
        """Deleting the entire data base if identified by name"""
        pass


    