Agri_Empower Learning API Contract
Version: v1.0
Owner: Smart Farming Platform Backend
Frontend Consumer: Agri_Empower Learning Engine
Status: Active
Last Updated: 2026-02-27


----------------------------------------
## Base URL

/api/v1/


----------------------------------------
## Endpoint

GET /api/v1/learning/<enterprise>/


Description:
Returns structured learning content for a specific enterprise.


----------------------------------------
## Path Parameters

enterprise:
- lowercase
- underscore allowed

category:
- lowercase
- optional (if using extended route)

topic:
- lowercase
- optional



{
  "production": {
    "title": "Production",
    "levels": {
      "foundation": {
        "summary": "string",
        "content": ["string"],
        "pdf": "string (optional)",
        "video": "string (optional)"
      },
      "intermediate": {},
      "advanced": {},
      "specialisation": {}
    }
  },
  "processing": {
    "title": "Processing",
    "levels": {}
  },
  "agribusiness": {
    "title": "Agribusiness",
    "levels": {}
  }
}

topic:
- lowercase
- underscore allowed (e.g., food_crops, land_animals)

enterprise:
- lowercase
- underscore allowed

pillar:
- production
- processing
- agribusiness

level:
- foundation
- intermediate
- advanced
- specialisation

Response Format (MUST MATCH EXACTLY)

{
  "production": {
    "title": "Production",
    "levels": {
      "foundation": {
        "summary": "string",
        "content": ["string"],
        "pdf": "string (optional)",
        "video": "string (optional)"
      },
      "intermediate": {},
      "advanced": {},
      "specialisation": {}
    }
  },
  "processing": {
    "title": "Processing",
    "levels": {}
  },
  "agribusiness": {
    "title": "Agribusiness",
    "levels": {}
  }
}

----------------------------------------
## Response Format (MUST MATCH EXACTLY)

{ ... your JSON structure ... }

----------------------------------------
## Rules

- All keys must be lowercase.
- No wrapper object.
- No pagination.
- No metadata fields in v1.
- Missing levels must return empty object {}.

----------------------------------------
## Error Responses

404 – Enterprise Not Found
{ "error": "Enterprise not found" }

400 – Invalid learning path
{ "error": "Invalid learning path" }
## Error Responses

  "error": "Invalid learning path"
}