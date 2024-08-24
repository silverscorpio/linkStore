## Link Store

Web application for storing and managing link/url-based information

#### An approach to solving to a personal problem with storing info gathered from the web

---

### Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [Stack](#stack)
- [Status](#status)

---

#### Purpose

- Having used several note-taking apps, like Evernote, OneNote, Notion, Apple Notes, note-taking still remained a pain
- Over the years, as more and more info was read on the web (primary source) and interesting ones had to be jotted down
  somewhere for later reference as well as me becoming a minimalist, the most preferred way of *taking notes* just
  boiled down to storing the URL/Link to that page with some notes, tags with further categorization under different
  topics
- Attempted to achieve this with Evernote, then later migrated to Notion and finally Apple Notes, have now tons of Links
  in different notes but still not properly organised - unhappy & not satisfied 😕
- Eventually after many thoughts and a lot of thinking, came up with the *LinkStore* idea

#### Features

- Minimalist method for note-taking/referencing/bookmarking from the web
- Allows storing info using the links for later reference
- Accompanying metadata - stored on, user-linked etc.
- Allows automatic extraction of title from URL, link type processing in most cases
- Authentication system (BasicAuth)
- Links in linkstore can be tagged as well grouped into topics
- Can be read and marked/starred
- If needed, personal notes per link can be added and stored
- Links, topics and tags have the CRUD functionality allowing their management

#### Stack

Python & Django, PostgreSQL for DB, Bootstrap (django-bootstrap) for frontend styling

#### Status

- project is being maintained and actively worked upon
- new frontend - design, views etc.
- backend - new features like search etc.
