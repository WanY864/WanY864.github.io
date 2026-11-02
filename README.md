# Yan Wan — M2 Courses

Hugo + Blowfish site for ten M2 Virtual & Augmented Reality courses.

**Public website:** https://wany864.github.io/

## Courses

1. [Advanced Computer Vision & 3D Reconstruction](content/courses/advanced-computer-vision-3d-reconstruction/_index.md)
2. [Artificial Intelligence](content/courses/artificial-intelligence/_index.md)
3. [Augmented Reality](content/courses/augmented-reality/_index.md)
4. [Basic Computer Vision](content/courses/basic-computer-vision/_index.md)
5. [Collaborative Environments](content/courses/collaborative-environments/_index.md)
6. [Computer Graphics](content/courses/computer-graphics/_index.md)
7. [Human-Computer Interface](content/courses/hci/_index.md)
8. [Social Robotics](content/courses/social-robotics/_index.md)
9. [Transversal Project](content/courses/transversal-project/_index.md)
10. [Virtual Reality](content/courses/virtual-reality/_index.md)

The Human-Computer Interface course keeps the existing `content/courses/hci/` directory. Its homework and lab pages have not been moved or renamed.

## URL compatibility

The site remains in the same repository: `WanY864/WanY864.github.io`. The website address and existing links remain unchanged, including:

- `/courses/hci/`
- `/courses/hci/homework-1/`
- `/courses/hci/homework-2/`
- `/courses/hci/lab-1a/`
- `/courses/hci/lab-1b/`
- `/courses/hci/lab-unity-ml-agent/`
- `/courses/hci/lab-mobile/`

## Add coursework

Each course has a folder under `content/courses/`. Add a Markdown page bundle for an assignment, lab, or project. For example:

~~~text
content/courses/artificial-intelligence/assignment-1/
  index.md
  experiment.png
~~~

Example page front matter:

~~~yaml
---
title: "Assignment 1"
date: 2026-11-01
draft: false
weight: 10
workType: homework
workStatus: in-progress
workSubtitle: "A short description of the work."
summary: "Short description of the assignment."
---
~~~

Edit the article body with actual work, screenshots, and reflections. Set `workType` to `homework`, `lab`, `project`, or `note` so the work appears automatically inside the relevant course page block. `workStatus` is optional (`completed` or `in-progress`), and `weight` controls ordering within each block. The homepage highlights selected published HCI homework and lists all ten courses, with courses containing published work first.

The new page is published when pushed to `main`, unless `draft: true` is set. Placeholder course sections are published to make navigation ready, but do not claim any coursework is already completed.

## Local preview (Windows)

Install Hugo Extended and Git. From the project directory, run:

~~~powershell
.\setup-theme.ps1
hugo server -D
~~~

Open `http://localhost:1313/`. You can also use `start-local.cmd`.

The Blowfish theme is already included under `themes/blowfish/` as regular project files, not as a Git submodule. `setup-theme.ps1` checks the theme and downloads it only if it is missing.

## Deployment

GitHub Actions builds the site when changes are pushed to `main`. The workflow is in `.github/workflows/hugo.yaml`, and repository Pages should use **Settings → Pages → Source → GitHub Actions**.

The public URL remains `https://wany864.github.io/`. The Hugo `baseURL` is set to the same address; the deployment workflow also uses the Pages-provided base URL.

## Content and image attribution

Use real lab observations, screenshots, and test results rather than inventing evidence. For third-party images, cite the original source where appropriate.

## Quality checks

Pull requests build the Hugo site and run `python3 scripts/check_site.py public` to check generated links, anchors, and image alt attributes. PRs also produce a downloadable preview artifact; only pushes to `main` deploy the website.

## Images and SEO

Article images are resized and converted to WebP in the site-level Markdown image render hook. Original page-bundle images remain available when visitors zoom in. Page descriptions are configured in `config/_default/`.
