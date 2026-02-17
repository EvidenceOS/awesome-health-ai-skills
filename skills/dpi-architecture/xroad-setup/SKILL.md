---
name: xroad-setup
description: Install and configure an X-Road Security Server for health data exchange
category: dpi-architecture
raigh_tier: tier-2
difficulty: advanced
estimated_time: "8 hours"
prerequisites: [fhir-resource-basics]
tags: [xroad, dpi, interoperability, security-server, data-exchange, estonia]
evidence_basis: "https://x-road.global/"
version: "1.0"
---

# X-Road Security Server Setup

## Purpose

X-Road is the backbone of Estonia's digital society and is deployed in 30+ countries for secure, auditable data exchange between organizations. In health, X-Road enables hospitals, labs, pharmacies, and insurers to share patient data securely. This skill teaches you to install and configure an X-Road Security Server — the gateway through which your organization joins the national data exchange.

## Learning Objectives

1. Explain X-Road architecture (Central Server, Security Server, Information Systems)
2. Install X-Road Security Server on Ubuntu
3. Register a subsystem and configure access rights
4. Make your first secure service call between two organizations
5. Understand the audit trail and how X-Road ensures accountability

## Context

For AIDA (African Institute for Interoperability Solutions), X-Road is the reference architecture for building continental health data exchange. Every country that joins the Pan-African health data network will need X-Road Security Servers at key health institutions. This skill is required for DPI architects deploying interoperability infrastructure.

## Steps

### Step 1: Understand X-Road Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   X-Road Ecosystem                       │
│                                                          │
│  ┌─────────────┐     ┌──────────────┐     ┌──────────┐ │
│  │ Hospital A   │     │ Central      │     │ Lab B    │ │
│  │ Info System  │     │ Server       │     │ Info     │ │
│  │     ↕        │     │ (Trust       │     │ System   │ │
│  │ Security     │←───→│  Anchor)     │←───→│    ↕     │ │
│  │ Server A     │     │              │     │ Security │ │
│  │              │     │              │     │ Server B │ │
│  └─────────────┘     └──────────────┘     └──────────┘ │
│                                                          │
│  Every message: encrypted, signed, timestamped, logged   │
└─────────────────────────────────────────────────────────┘
```

Key concepts:
- **Security Server**: Gateway that encrypts, signs, and logs all data exchange
- **Central Server**: Trust anchor that manages the member directory
- **Subsystem**: A logical service within your organization (e.g., "Patient Registry")
- **Service**: An API endpoint exposed through X-Road

### Step 2: Install Security Server

On Ubuntu 22.04 LTS:

```bash
# Add X-Road repository
sudo apt-get update
sudo apt-get install -y curl gnupg
curl https://artifactory.niis.org/api/gpg/key/public | sudo apt-key add -

# Add repository (use the test environment for learning)
echo "deb https://artifactory.niis.org/xroad-release-deb jammy-7.4 main" | \
  sudo tee /etc/apt/sources.list.d/xroad.list

# Install
sudo apt-get update
sudo apt-get install -y xroad-securityserver

# Access admin UI
# https://your-server:4000 (default admin interface)
```

### Step 3: Initial Configuration

In the Security Server admin UI:
1. **System Parameters**: Set the Security Server address and instance identifier
2. **Timestamping Service**: Configure timestamping provider
3. **Signing Keys**: Generate or import signing and authentication keys
4. **Certificate Authority**: Register your certificate with the Central Server
5. **Members**: Register your organization as an X-Road member

### Step 4: Register a Health Subsystem

Create a subsystem for your health information system:
- Member: `GOV/MINISTRY-OF-HEALTH` (or your organization identifier)
- Subsystem: `PATIENT-REGISTRY`
- Service: `getPatientByIdentifier`

Configure access rights:
- Who can call this service? (e.g., only registered hospitals)
- What data is returned? (e.g., FHIR Patient resource)
- Audit logging: Every call is logged with caller, timestamp, and response code

### Step 5: Make Your First Service Call

Using a test client, make a secure service call:

```bash
# X-Road service call (SOAP or REST)
curl -X GET \
  -H "X-Road-Client: INSTANCE/GOV/HOSPITAL-A/EHR" \
  -H "X-Road-Id: unique-request-id" \
  "https://security-server-a:8443/r1/INSTANCE/GOV/MOH/PATIENT-REGISTRY/getPatientByIdentifier?id=UL-MED-2026-0042"
```

Verify:
- [ ] Request was encrypted in transit
- [ ] Both parties' signatures are in the message log
- [ ] Timestamp is present
- [ ] Audit trail shows the request in both Security Servers

## Artifacts

1. **Architecture Diagram** — X-Road topology for your pilot setup (even if single-server test)
2. **Installation Log** — Screenshot or log of successful Security Server installation
3. **Subsystem Configuration** — Documentation of your registered subsystem and services
4. **Service Call Evidence** — Successful request/response with audit trail

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Installation | Security Server running and accessible | Installation failed or incomplete |
| Configuration | Subsystem registered with proper access rights | Missing access controls |
| Service call | Successful encrypted call with audit trail | Call fails or no audit trail |
| Architecture understanding | Can explain each component's role | Confused about architecture |

## Common Mistakes

- Skipping certificate configuration (X-Road requires proper PKI — no shortcuts)
- Opening too many ports (Security Server needs only 5500, 5577, 4000, 8443)
- Forgetting that X-Road is asynchronous — don't assume instant responses
- Not testing the audit trail — the audit log is the whole point of X-Road

## Related Skills

- `fhir-resource-basics` — Services should return FHIR-formatted data
- `dhis2-adx-export` — DHIS2 data can be exchanged via X-Road
- `openhim-mediator` — OpenHIM can act as an X-Road consumer

## References

- X-Road Documentation: https://docs.x-road.global/
- X-Road Academy: https://x-road.global/xroad-academy
- NIIS (Nordic Institute for Interoperability Solutions): https://niis.org/
