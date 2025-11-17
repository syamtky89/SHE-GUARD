# SHE-GUARD — Women’s Safety Multi-Agent AI System

A Python-based multi-agent framework designed to improve women’s safety through
autonomous threat detection, location intelligence, emergency response, and
evidence collection.

---

## 🔥 Features
- AI-driven risk detection  
- GPS + safe zone guidance  
- Emergency SMS + simulated call  
- Evidence logging (timestamps, events)  
- Fully modular multi-agent architecture  

---

## 🧠 Agents Overview

### **Supervisor Agent**
Coordinates all other agents and executes decision logic.

### **Risk Agent**
Analyzes user messages and assigns a threat score (0–100).

### **Location Agent**
Provides GPS coordinates + nearest safe locations.

### **Emergency Agent**
Sends emergency SMS + calls police control room.

### **Evidence Agent**
Records all events with timestamps.

---

## 🚀 Run the App

```bash
python main.py
