<div align="center">

# HTTP Methods Reference

</div>

---

## Methods Overview

| Method | Body | Safe | Idempotent | Purpose |
|:-------|:----:|:----:|:----------:|:--------|
| GET | No | Yes | Yes | Retrieve resource |
| POST | Yes | No | No | Create resource |
| PUT | Yes | No | Yes | Replace resource |
| PATCH | Yes | No | No | Partial update |
| DELETE | No | No | Yes | Remove resource |
| HEAD | No | Yes | Yes | Get headers only |
| OPTIONS | No | Yes | Yes | Get allowed methods |

---

## Usage Examples

```bash
# GET - Retrieve data
curl http://api.example.com/users/1

# POST - Create resource
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Sifuna"}' http://api.example.com/users

# PUT - Update resource (full)
curl -X PUT -H "Content-Type: application/json" \
  -d '{"name":"Sifuna","email":"new@example.com"}' \
  http://api.example.com/users/1

# PATCH - Partial update
curl -X PATCH -H "Content-Type: application/json" \
  -d '{"email":"updated@example.com"}' \
  http://api.example.com/users/1

# DELETE - Remove resource
curl -X DELETE http://api.example.com/users/1

# OPTIONS - Get allowed methods
curl -X OPTIONS -I http://api.example.com/users
```

---

## Security Notes

```
GET    - Never modify data, never send credentials in URL
POST   - Always use CSRF tokens, validate input
PUT    - Require authentication, validate ownership
DELETE - Require authentication, confirm destructive action
OPTIONS - Used for CORS preflight, configure properly
```
