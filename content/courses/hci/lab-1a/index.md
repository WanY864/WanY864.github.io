---
title: "HCI — Lab 1A: Building My Course Website"
date: 2026-10-01
summary: "Building and publishing my HCI course portfolio with Hugo, Blowfish, GitHub Desktop, and GitHub Pages."
tags: ["HCI", "Lab", "Hugo", "Blowfish", "GitHub Pages"]
categories: ["Human-Computer Interaction"]
draft: false
showTableOfContents: true
---

## Goal

The goal of this lab was to create an online course portfolio that I can update throughout the semester.

I used **Hugo** as the static-site generator and **Blowfish** as the theme. The final website is published with **GitHub Pages**, so the coursework can be accessed through a normal public URL instead of only from a local development server.

## Tools

- Hugo Extended
- Blowfish
- Git
- GitHub Desktop
- GitHub Pages

## Process

I first installed Hugo Extended and created the website locally. I then organised the content into a simple course structure:

```text
content/
└── courses/
    └── hci/
        ├── homework-1/
        ├── lab-1a/
        └── lab-1b/
```

The site was configured as a compact academic portfolio rather than a general-purpose blog. I used a white background, restrained blue accents, thin separators, smaller article navigation, and lightweight hover transitions.

For local testing, I used:

```text
hugo server -D
```

The website could then be previewed at:

```text
http://localhost:1313/
```

After the local version worked, I created the repository **WanY864.github.io** and used GitHub Desktop to upload the project. GitHub Actions then built the Hugo site and deployed it to GitHub Pages.

## Problems and Solutions

### 1. Blowfish theme was not found

The first major problem occurred when Hugo reported:

```text
module "blowfish" not found
```

The original setup attempted to install Blowfish as a Git submodule, but the repository did not contain a valid `.gitmodules` configuration. This caused the theme installation to fail even though the setup script continued running.

I fixed this by changing the setup method so that Blowfish was downloaded directly into:

```text
themes/blowfish
```

This removed the dependency on Git submodules and made the project easier to move and publish.

### 2. GitHub Desktop initially showed nothing to upload

The GitHub Pages repository already existed online, while my website files were stored in a different local folder. GitHub Desktop therefore had no changes to commit.

I solved this by cloning the online repository with GitHub Desktop and then copying the website files into the cloned repository folder. After that, GitHub Desktop detected the files correctly and allowed me to commit and push them.

### 3. GitHub Pages showed two deployment workflows

After the first upload, GitHub displayed both the custom Hugo workflow and the default Pages build process. The default process failed, but the custom Hugo workflow succeeded.

The important setting was:

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```

The custom workflow successfully completed the build, artifact upload, and deployment stages.

## Design Decisions

I wanted the website to feel closer to an academic course portfolio than a generic personal blog.

The main visual decisions were:

- a clean white layout,
- compact typography,
- subtle blue divider lines,
- lightweight motion on links and content blocks,
- a smaller right-side table of contents,
- and direct navigation to course work.

These choices keep the interface visually quiet while still giving the pages a clear hierarchy.

## What I Learned

This lab helped me understand the separation between three layers of a static website:

1. **Content** — Markdown files and images.
2. **Theme** — Blowfish controls much of the layout and visual structure.
3. **Generator and deployment** — Hugo builds the site, while GitHub Pages publishes it.

I also learned that a website that works locally is not automatically ready for deployment. Theme installation, repository structure, and the GitHub Pages build source all have to be configured correctly.

The final result is a reusable course portfolio that can be updated by adding new Markdown pages and pushing the changes to GitHub.
