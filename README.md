# National Team Scouting & Eligibility Tracker

An end-to-end football analytics project designed to track national team eligibilty pipelines, player performance profiles, and automated recruitement metric indexing for international squad call-ups.

## Project Overview

Unlike club recruitment platforms that evaluate transfer market values, this platform models the specific administrative workflows of national federations using NFF as a case study. It builds a secure, structured respository separating fixed player heritage/citizenship metadata from dynamic weekely performance statistics. 

## System Architecture & Data Layer

The engineering structure uses a decoupled relational layout built with SQLite to manage data profiles cleanly without redundancy:

- players (Metadata Table): Tracks fixed player properties including nationality ties, current clubs, playing positions, and FIFA cap-tied status.

- stats (Metrics Table): Houses per-90 metrics (goals, assists, progressive passes, tackles, interceptions) linked contextually to the main metadata table via unique relational keys (player_id).