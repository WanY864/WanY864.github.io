---
title: "HCI — Lab 1B: Unity Setup"
date: 2026-10-01
summary: "Preparing the Unity development environment and the workflow for my first 3D project."
tags: ["HCI", "Lab", "Unity"]
categories: ["Human-Computer Interaction"]
draft: false
showTableOfContents: true
---

## Goal

The goal of this lab is to prepare the Unity development environment and create a first working 3D project.

The setup is kept separate from the website project so that Unity editors, downloads, and project files can be managed independently.

## Environment Structure

To keep large Unity files away from the system drive, I planned the following structure on drive `D:`:

```text
D:\Unity\
├── Editors\
├── Downloads\
└── Projects\
```

Unity Hub can remain installed normally, while the large Editor installations and project files can be placed on the secondary drive.

## Setup Procedure

The Unity setup workflow is:

1. Install Unity Hub.
2. Sign in with a Unity account if required.
3. Set the Unity Editor installation location to `D:\Unity\Editors`.
4. Set the download/cache location to `D:\Unity\Downloads`.
5. Install a stable Unity Editor version.
6. Create a new 3D project inside `D:\Unity\Projects`.
7. Open the project and inspect the main Unity panels.
8. Add a simple 3D object to the scene.
9. Change its position, rotation, and scale.
10. Enter Play Mode and verify that the scene runs correctly.

## Main Unity Panels

For the first project, the most important parts of the interface are:

### Hierarchy

The Hierarchy lists the objects currently contained in the scene.

### Scene

The Scene view is the main workspace used to place and edit objects.

### Inspector

The Inspector shows the properties and components of the selected object.

### Game

The Game view shows what the active camera outputs when the project runs.

Understanding the difference between the Scene view and the Game view is important: the Scene view is used to build the environment, while the Game view represents the runtime result.

## First Project Checklist

The first project should contain at least:

- one simple 3D object,
- a working camera,
- a light source,
- basic transform changes,
- and a successful Play Mode test.

## Documentation

The final lab evidence should include screenshots of:

- Unity Hub,
- the installed Unity Editor,
- the New Project window,
- the Unity Editor interface,
- the first 3D scene,
- and the project running in Play Mode.

These screenshots provide direct evidence that the environment is installed and the first project is working.

## What I Learned

The main lesson from the setup process is that Unity becomes easier to understand when the interface is treated as a small workflow rather than as one large application:

```text
Create object
→ Select object
→ Edit in Inspector
→ Arrange in Scene
→ Check in Game view
→ Run in Play Mode
```

This workflow provides a clear starting point before moving on to more advanced interaction, scripting, or XR development.
