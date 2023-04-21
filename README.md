# Quest journey - self generating story rpg game

Quest journey is an open project - frames are defined but can easily be changed. Based on most recent works made in AI area I wanted to implement new tools and see possibility that comes with it.

That's the "Quest journey" - app that can be a Game Master, will come up with a story for RPG game and will implement new events up to the final outcomes. The main idea is to create a small engine that will generate content - story - based on human interaction.

## Technology:

Python - libraries(os, typing, NumPy, OpenAI, TTS, mysql, openai-whisper)

frame:
- self generating content (text) based on initial input, like adjectives.
- based on provided text generating hero classes and other.
- story generation influenced by players actions.
- generation of objects, classes, npc and events based on "prologue", "location", "player" and "actions".
- generation of voice based on new text from AI engine.
- using whisper voice to text recognition.

## In progress:

- GameObject class - "parent" - define all attributes that GameObject needs.
- RPGScenario(GameObject) class - "child" - define scenario.
- Database class - define operations on MySQL database.
- Make class - define OpenAI API communication.

## To do:

- in the future training model on data to prepare it for text generation without OpenAI API servers,
- that also counts for TTS - right now in use are models provided in library, but they seem a little harsh,
- making other classes (turn, hero classes, combat, explore, backpack, influence - ability to generate new outcomes, role).

## Classes:

Here will be documented definition of each class.

- turn,
- classes,
- combat,
- explore,
- backpack,
- influence

## Contributing

Report bugs...

## License

MIT License

Copyright (c) [2023] [kanies89]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



