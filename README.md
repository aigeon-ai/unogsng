# uNoGSNG MCP Server

Welcome to the uNoGSNG MCP Server, your comprehensive tool for navigating and utilizing the Next Generation Netflix Global Search capabilities. This server offers a cleaner and more intuitive experience for accessing Netflix data, allowing you to efficiently search, retrieve, and analyze information from across Netflix's global catalog.

## Overview

uNoGSNG is designed to streamline the process of accessing Netflix content data, providing a robust set of tools to enhance your search and retrieval capabilities. This server operates under a freemium model, allowing for basic access with optional upgrades for more extensive use.

### Key Features

- **Popularity:** Rated 9.9 for its reliability and efficiency.
- **Service Level:** Maintains a 100% service level to ensure constant availability.
- **Latency:** Operates with an average latency of 463ms, ensuring quick responses to your queries.

## Tools and Functions

The uNoGSNG MCP Server offers a variety of tools organized into different categories to help you access and manipulate Netflix data efficiently:

### Static Tools
- **Genres:** Retrieve a list of Netflix genres to categorize and filter content.
- **Countries:** Access a list of available Netflix countries, including uNoGS-specific country IDs.

### Search Tools
- **People:** Search for Netflix personalities by name, returning person IDs for further exploration.
- **Deleted Titles:** Access a list of titles that have been removed, filtered by specific criteria.
- **Search:** Perform comprehensive searches for Netflix titles using a variety of parameters, such as genre, year, and country.

### Details Tools
- **Images:** Retrieve all images associated with a specific Netflix title.
- **Title Countries:** Get a list of countries where a particular Netflix ID is available.
- **Title Genres:** Discover all genres associated with a specific Netflix ID.
- **Title Details:** Obtain specific information about a given Netflix title.
- **Expiring Titles:** Identify titles that are nearing expiration.
- **Episodes:** Search for episodes related to a Netflix title or personality.

## Usage Guidelines

- **Country List:** When using the `countrylist` query, it assumes a list of uNoGS-specific country IDs. These can be obtained using the `/country` endpoint. If left blank, the server assumes you want to match all countries.
- **Limits and Offsets:** Results are limited to the first 100 entries by default. Adjust this number with the `limit` query parameter. To paginate results, use multiples of the limit as the `offset` parameter.
- **Search Parameters:** Utilize powerful search functions allowing you to specify complex queries such as `country_andorunique` and `newdate` to refine your search results.

uNoGSNG MCP Server is a powerful tool for anyone needing to navigate and utilize Netflix’s global content efficiently. Whether you're tracking content availability, exploring genres, or retrieving detailed information about specific titles, uNoGSNG provides the capabilities you need to get the job done.