# Database and Security

## PostgreSQL

PostgreSQL is the project database. Development Compose configuration creates:

- Database: `agrimarket`
- User: `agrimarket`
- Port: `5432`

Credentials are configurable through `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, and `POSTGRES_PORT`.

## Planned relational model

```text
User
Farmer -> User
FPO -> User
Buyer -> User
Commodity
Market
MarketPrice -> Market, Commodity
MarketArrival -> Market, Commodity
Lot -> Farmer or FPO, Commodity
QualityGrade
BuyerRequirement -> Buyer, Commodity
Offer -> Lot, Buyer
TransportOption
StorageFacility
Transaction -> Lot, Buyer
Payment -> Transaction
Prediction -> Commodity, Market
Recommendation -> Lot or User
Grievance -> User, Transaction
```

## Data integrity

- Use foreign keys for ownership and lifecycle relationships.
- Use decimal fields for prices and monetary values.
- Store timestamps with timezone awareness.
- Keep source, observed date, and ingestion metadata for market data.
- Add status transition validation for lots, offers, transactions, and grievances.
- Avoid deleting financial or dispute records; use archival/status changes.

## Security requirements

- JWT authentication
- Role-based access control for farmer, FPO, buyer, and admin roles
- Password hashing through Django authentication
- Server-side request validation
- Rate limiting for authentication and offer endpoints
- Audit logging for offers, negotiations, payments, and status changes
- Secure upload validation for verification documents
- Secret values supplied through environment variables
- HTTPS, secure cookies, and restrictive CORS in production
- Protection of personal, payment, and identity information

The current MVP has development settings only. Production security controls must be implemented before deployment.
