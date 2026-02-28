Agri_Empower Learning API Contract
Version: v1.0
Owner: Smart Farming Platform Backend
Frontend Consumer: Agri_Empower Learning Engine
Status: Active
Last Updated: 2026-02-27

GET /api/v1/learning/<category>/<topic>/<enterprise>/

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

Rules:
- All keys must be lowercase.
- No wrapper object (e.g., no {"data": {...}})
- No pagination.
- No metadata fields.
- Missing levels must return empty object {}.

## Error Responses

404 – Enterprise Not Found

{
  "error": "Enterprise not found"
}

400 – Invalid category/topic/enterprise combination

{
  "error": "Invalid learning path"
}