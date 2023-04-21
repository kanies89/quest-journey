from class_gameobject import GameObject
from game_db import Database
from typing import List, Type, Tuple
from txt_to_voice import txt_tov
import os
import subprocess

class RPGScenario(GameObject, Database):
    table_name: str = "rpg_scenario"
    fields: List[Tuple[str, Type]] = [("title", str), ("prologue", str), ("prologue_audio", str), ("player_count", int)]

    def __init__(self, title: str, prologue: str, player_count: int, prologue_audio: str = None):
        super().__init__(title, prologue, prologue_audio, player_count)

    @classmethod
    def get_schema(cls) -> str:
        return f"id INTEGER PRIMARY KEY AUTO_INCREMENT, title TEXT, prologue TEXT, prologue_audio TEXT, player_count INTEGER"

class TextToVoice:
    def __init__(self, db):
        self.db = db

    def generate_audio(self, game_obj, column):
        # Generate filename based on table name, column name, and ID
        filename = f"{game_obj.table_name}_{column}_{game_obj.id}.wav"

        # Check if the file already exists
        if os.path.isfile(filename):
            return filename

        # Get the text from the specified column of the game object
        text = getattr(game_obj, column)

        # Call the text-to-voice program to generate the audio file
        txt_tov(filename, text)

        # Save the filename in the database
        c = self.db.conn.cursor()
        c.execute(f"UPDATE {game_obj.table_name} SET {column}_audio=%s WHERE id=%s", (filename, game_obj.id))
        self.db.conn.commit()

        return filename
