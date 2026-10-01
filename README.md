# Yan Wan — HCI Course Portfolio

A ready-to-use **Hugo + Blowfish** project for the HCI course. The site content is English-only and uses a clean white layout with restrained blue accent lines.

## Recommended folder on Windows

Unzip the project to:

```text
D:\HCI-Blog
```

The project itself, images, and future homework posts can stay on drive `D:`.

## First run

You need **Hugo Extended** and **Git** available in Windows `PATH`.

Open PowerShell in `D:\HCI-Blog` and run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\setup-theme.ps1
hugo server -D
```

Then open:

```text
http://localhost:1313/
```

The first command installs the Blowfish theme as a Git submodule. After that, normal local previews only need:

```powershell
hugo server -D
```

You can also double-click `start-local.cmd`; it runs the setup check and starts the preview server.

## Site structure

```text
HCI-Blog/
├── assets/
│   └── css/
│       └── custom.css
├── config/
│   └── _default/
│       ├── hugo.toml
│       ├── languages.en.toml
│       ├── markup.toml
│       ├── menus.en.toml
│       └── params.toml
├── content/
│   ├── _index.md
│   ├── about/
│   │   └── index.md
│   └── courses/
│       ├── _index.md
│       └── hci/
│           ├── _index.md
│           ├── homework-1/
│           │   ├── index.md
│           │   ├── traditional-screwdrivers.png
│           │   ├── electric-screwdriver.png
│           │   ├── laptop-screen-film.png
│           │   ├── canva-website-builder.png
│           │   ├── cookie-banner-dark.svg
│           │   ├── cookie-banner-redesign.svg
│           │   ├── newsletter-nagging.svg
│           │   └── newsletter-redesign.svg
│           ├── lab-1a/
│           │   └── index.md
│           └── lab-1b/
│               └── index.md
├── .github/workflows/hugo.yaml
├── setup-theme.ps1
└── start-local.cmd
```

## What is already finished

`HCI — Homework 1` is publishable (`draft: false`) and already contains:

- Affordance: traditional screwdriver vs. electric screwdriver controls;
- Gestalt Case 1: laptop screen film / figure-ground;
- Gestalt Case 2: Canva website-builder page / similarity + figure-ground;
- Dark Pattern 1: interface interference in an unequal cookie banner;
- Dark Pattern 2: nagging through a repeated newsletter pop-up;
- redesigns for both dark-pattern examples.

## Lab pages

`Lab 1A` and `Lab 1B` remain `draft: true` deliberately.

The HCI homework is based on analysis and can be completed in advance. The lab pages, however, ask you to document the **actual process**, including real problems and how you solved them. After you finish the site deployment and Unity setup, add your real screenshots and notes, then change:

```toml
draft: true
```

to:

```toml
draft: false
```

## Publish with GitHub Pages

Create an empty GitHub repository, then from the project folder run:

```powershell
git add .
git commit -m "Initial HCI course portfolio"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

In GitHub repository settings:

```text
Settings → Pages → Source → GitHub Actions
```

The included `.github/workflows/hugo.yaml` builds and deploys the site automatically. After the workflow finishes, your public URL will normally be `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`.

## Image note

The four main Homework 1 images are the images supplied for the coursework. If any of them came from the web, add the original source URL to the relevant figure caption before final submission.


## Visual refinements in this version

- Tighter homepage spacing
- More blue separator lines and cleaner visual rhythm
- Smaller right-side table of contents typography
- Smoother transitions on links, images, and content blocks


## If theme setup previously failed

Version 4 no longer uses Git submodules. It downloads Blowfish into `themes/blowfish`
as normal project files, which avoids `.gitmodules` errors.

If you are upgrading an existing folder, delete any incomplete `themes/blowfish`
folder first, then run:

```powershell
.\setup-theme.ps1
hugo server -D
```
