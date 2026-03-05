Agri_Empower Learning API Contract
Version: v1.0
Owner: Smart Farming Platform Backend
Frontend Consumer: Agri_Empower Learning Engine
Status: Active
Last Updated: 2026-02-27

--------------------------------------------------
## Base URL

/api/v1/

--------------------------------------------------
## Endpoint

GET /api/v1/learning/<enterprise>/

Description:
Returns structured learning content for a specific enterprise.

--------------------------------------------------
## Path Parameters

enterprise:
- required
- lowercase
- underscore allowed (e.g., tomato_farming, rabbit_production)

--------------------------------------------------
## Response Format (MUST MATCH EXACTLY)

{
  "production": {
    "title": "Production",
    "levels": {
      "foundation": {
        "summary": "string",
        "content": ["string"],
        "pdf": "string (optional, full URL)",
        "video": "string (optional, full URL)"
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

--------------------------------------------------
## Field Definitions

pillar:
- production
- processing
- agribusiness

level:
- foundation
- intermediate
- advanced
- specialisation

content:
- plain text only
- array of paragraph strings

pdf:
- must be full downloadable URL

video:
- must be full URL (YouTube or hosted link)

--------------------------------------------------
## Rules

- All keys must be lowercase.
- No wrapper object (no {"data": {...}}).
- No pagination.
- No metadata fields in v1.
- Missing levels must return empty object {}.
- Missing pillars must still appear with empty structure.

--------------------------------------------------
## Error Responses

404 – Enterprise Not Found
{
  "error": "enterprise not found"
}

400 – Invalid enterprise format
{
  "error": "invalid learning path"
}
