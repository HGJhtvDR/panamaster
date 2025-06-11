"""
Модуль для безопасной обработки файлов.
"""

import os
from werkzeug.utils import secure_filename
from typing import List, Tuple
import magic  # python-magic для определения MIME-типов

class FileProcessor:
    ALLOWED_EXTENSIONS = {
        'image': {'png', 'jpg', 'jpeg', 'gif'},
        'document': {'pdf', 'doc', 'docx'},
        'archive': {'zip', 'rar'}
    }
    
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

    def __init__(self):
        self.mime = magic.Magic(mime=True)

    def is_allowed_file(self, filename: str, file_type: str = 'image') -> bool:
        """
        Проверка разрешенных расширений файла.
        
        Args:
            filename (str): Имя файла
            file_type (str): Тип файла (image, document, archive)
            
        Returns:
            bool: True если файл разрешен
        """
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS.get(file_type, set())

    def secure_filename(self, filename: str) -> str:
        """
        Безопасное имя файла.
        
        Args:
            filename (str): Исходное имя файла
            
        Returns:
            str: Безопасное имя файла
        """
        return secure_filename(filename)

    def validate_file(self, file_path: str) -> Tuple[bool, str]:
        """
        Валидация файла.
        
        Args:
            file_path (str): Путь к файлу
            
        Returns:
            tuple: (bool, str) - результат валидации и сообщение
        """
        if not os.path.exists(file_path):
            return False, "Файл не найден"
            
        if os.path.getsize(file_path) > self.MAX_FILE_SIZE:
            return False, "Файл слишком большой"
            
        mime_type = self.mime.from_file(file_path)
        # TODO: Добавить проверку MIME-типа
        
        return True, "Файл валиден" 