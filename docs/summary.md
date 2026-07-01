# Project KRIYA: Executive Summary

**Project Name:** KRIYA (Inbound Demand-Supply Matching Platform)

## 📋 Project Overview
**KRIYA** is a high-efficiency worker management and inbound demand-supply matching platform designed specifically for the SEA Movement NGO. It serves as a trusted, centralized mediator platform to handle blue-collar and field-based workforce logistics. 

Instead of an outbound scraping tool, KRIYA allows local businesses and contractors to submit their labor requirements (demand), which the NGO fulfills by deploying verified, pre-trained blue-collar workers from their roster (supply). It acts as an automated Applicant Tracking System (ATS) and dispatch center, ensuring safe livelihoods for workers and providing vetted talent for ethical employers. 

**Core Features:** Real-time attendance logging, task/shift tracking, and a robust operational dashboard.

---

## 🛠️ The Tech Stack (Zero-Cost, High-Performance)

The architecture is designed for maximum speed, efficiency, and robustness on lower-end mobile devices, while achieving a $0.00 hosting cost.

### 1. Frontend: Astro (Hosted on Vercel)
* **Architecture:** Leverages Astro's "Islands Architecture" to ship zero JavaScript by default. Highly interactive components (like the KRIYA attendance grids) are hydrated individually. This guarantees lightning-fast loading speeds on mobile browsers and lower-end devices out in the field.
* **Design & Layout:** Built using Tailwind CSS for a modern, responsive, and mobile-first interface.
* **Hosting:** Both frontends—the NGO Worker portal and the Admin Dashboard—will be hosted as separate projects under a single **Vercel Hobby Account** completely for free.
* **Role:** Handles the public-facing employer intake forms, worker registration layout, and all UI interfaces.

### 2. Backend: Rust with Axum (Hosted on AWS Lambda)
* **Architecture:** A **Modular Monolith**. Rather than managing separate microservices, a single Rust binary handles the logic for the whole platform using nested routing (e.g., `/dashboard/...` and `/ngo/...`). It manages database connections, authentication, and core business logic.
* **Performance:** Replaces traditional Python/Node environments to completely eliminate serverless "cold start" lag (dropping initial response times from seconds down to less than 50ms) with compile-time safety and incredible concurrency handling.
* **Hosting:** Deployed via `cargo-lambda` to **AWS Lambda**. Running at the minimum 128MB memory tier allows the AWS free tier to cover millions of execution seconds per month.

### 3. Database: Supabase (PostgreSQL)
* **Storage:** Managed PostgreSQL on Supabase's free tier.
* **Connection Safety:** The Axum backend uses the `sqlx` crate to connect securely via Supabase's **Transaction Pooler** (port 6543) instead of direct connections. This prevents connection drop errors or exhaustion even if hundreds of workers log in simultaneously.

### 4. AI-Assisted Development
* **Workflow:** Code scaffolding is driven by AI assistants (like Google AI Studio and Replit) acting as engineering co-pilots. Strict prompting for Axum and Astro will rapidly build out KRIYA's type-safe endpoints and frontend layouts.

---

## ⚙️ Core Workflows to Build

The KRIYA backend and frontend tightly integrate to manage three primary data flows:

1. **The Employer Intake (Demand)** 
   A clean, mobile-first form on Astro where local businesses submit requests (Job Type, Number of Workers Needed, Daily Wage, Location). This data is securely posted to the Axum API endpoints.
   
2. **The Worker Roster (Supply)**
   A secure database layer managed by Axum tracking worker profiles, specialized skills, and their live availability lifecycle state (e.g., *In Training*, *Ready for Placement*, *Currently Deployed*).

3. **The Matching & Dispatch Engine** 
   The core internal logic written in Rust. When an employer request is submitted, Axum queries the PostgreSQL database, filters for available workers with matching skills, and populates a queue on the NGO Command Dashboard for manual approval and deployment.

---
**The Bottom Line:** KRIYA is an enterprise-grade application optimized to run flawlessly, scale instantly under heavy field usage, and cost exactly $0.00 in hosting fees.
