# Beyond-rss

I was bored with rss feed having tons of garbage articles so i designed this system to aggregate RSS feeds, process them using an AI model, and provide personalized content recommendations based on like/dislike of the articles.
Below is a comprehensive guide to understand, set up, and use this system effectively.

## Table of Contents

- [Beyond-rss](#beyond-rss)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Architecture](#architecture)
  - [Features](#features)
  - [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

The RSS Feed Recommendation System is built to enhance user experience by delivering tailored content recommendations sourced from subscribed RSS feeds. It utilizes AI models to process feed data and employs user interactions (like/dislike) to refine and personalize these recommendations over time.

## Architecture

The system architecture consists of several components:

- **Data Layer**: PostgreSQL or SQLite database stores user preferences, feed data, and processed information.
- **Network Layer**: Feed Fetcher component fetches RSS feeds periodically from subscribed sources.
- **AI Processing Layer**: AI Model processes fetched RSS feed data to generate content representations for recommendation.
- **User Interface Layer**:
  - **API Service**: Handles user interactions such as submitting preferences and receiving personalized recommendations.
  - **Web Application**: Provides a user-friendly interface for managing feed subscriptions, preferences, and interacting with recommended content.

The flow of data:

- Users interact with the Web Application or API Service to manage subscriptions and preferences.
- The Feed Fetcher fetches RSS feeds and stores them in the database.
- AI Model processes the fetched data and generates personalized recommendations based on user preferences stored in the database.

## Features

- **RSS Feed Aggregation**: Automatically fetches and updates RSS feed entries.
- **AI-driven Recommendations**: Uses AI models to generate personalized content recommendations.
- **User Preferences**: Collects and utilizes user feedback (like/dislike) to refine recommendations.

## Setup Instructions

To get started with the RSS Feed Recommendation System, follow these instructions:

### Prerequisites

- Docker installed on your machine.
- Git installed on your machine.
- Python 3.9 or higher installed locally (for development purposes).

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/beyond-rss.git
   cd rss-feed-recommendation
   ```

2. **Set up Docker containers**:

   ```bash
   docker-compose up --build
   ```

   This command will build and start the necessary Docker containers (`feed_fetcher`, `ai_processing`, `api_service`, `database`, etc.) as defined in `docker-compose.yml`.

3. **Access the Web Application**:

   - Once containers are up and running, access the Web Application by visiting `http://localhost:8000` in your web browser.

## Usage

1. **Subscribing to RSS Feeds**:

   - Use the Web Application to subscribe to RSS feeds of interest.
   - The Feed Fetcher will periodically fetch new entries from subscribed feeds.

2. **Managing User Preferences**:

   - Users can set preferences (keywords, categories) in the Web Application.
   - Use the like/dislike buttons to provide feedback on recommended articles.

3. **Viewing Recommendations**:
   - Based on user interactions, the AI Model generates personalized recommendations.
   - Recommendations are displayed in the Web Application based on user preferences and feedback.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or submit a pull request. For major changes, please discuss them first by opening an issue.

## License

This project is licensed under the [The Unlicense](LICENSE).

---
