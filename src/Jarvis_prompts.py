# Jarvis Command Processing Engine
# Memory System and Natural Language Processing
# Supports voice commands and text input

import json
import os
from datetime import datetime
from pathlib import Path


class MemorySystem:
    """Persistent memory storage for conversation history"""
    
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.load_memory()
    
    def load_memory(self):
        """Load existing memory from file"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    self.memory = json.load(f)
            except:
                self.memory = {"entries": []}
        else:
            self.memory = {"entries": []}
    
    def save_memory(self):
        """Save memory to file"""
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)
    
    def add_entry(self, message, response, context=None):
        """Add a new memory entry"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "response": response,
            "context": context or {}
        }
        self.memory["entries"].append(entry)
        self.save_memory()
    
    def get_recent(self, limit=5):
        """Get recent conversation entries"""
        return self.memory["entries"][-limit:]


class CommandProcessor:
    """Process and execute commands"""
    
    def __init__(self):
        self.memory = MemorySystem()
        self.commands = {
            "help": self.cmd_help,
            "status": self.cmd_status,
            "memory": self.cmd_memory,
            "clear": self.cmd_clear
        }
    
    def process_command(self, text):
        """Process user command or text"""
        command = text.lower().strip()
        
        if command in self.commands:
            response = self.commands[command]()
        else:
            response = self.process_natural_language(text)
        
        self.memory.add_entry(text, response)
        return response
    
    def cmd_help(self):
        return "Available commands: help, status, memory, clear"
    
    def cmd_status(self):
        return "Jarvis AI Assistant - All systems operational"
    
    def cmd_memory(self):
        recent = self.memory.get_recent()
        return f"Retrieved {len(recent)} recent entries from memory"
    
    def cmd_clear(self):
        self.memory.memory = {"entries": []}
        self.memory.save_memory()
        return "Memory cleared"
    
    def process_natural_language(self, text):
        """Process natural language input"""
        keywords = ["open", "close", "run", "launch", "start", "stop"]
        
        for keyword in keywords:
            if keyword in text.lower():
                return f"Processing command with keyword: {keyword}"
        
        return "Command acknowledged. Processing..."


def main():
    processor = CommandProcessor()
    print("Jarvis Command Processor Initialized")
    print("Type 'help' for available commands")
    
    while True:
        user_input = input("\nJarvis> ").strip()
        if user_input.lower() == "quit":
            break
        
        response = processor.process_command(user_input)
        print(f"Response: {response}")


if __name__ == "__main__":
    main()
