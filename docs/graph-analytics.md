# Graph Analytics

## Purpose

GraphX can represent relationships among farmers, FPOs, markets, buyers, warehouses, processors, and transport routes. This supports network-level analysis beyond individual price comparisons.

## Graph model

Vertices:

- Farmer
- FPO
- Market
- Buyer
- Warehouse
- Processing unit

Edges:

- `AGGREGATES`
- `SELLS_TO`
- `BUYS_FROM`
- `SUPPLIES_TO`
- `STORES_AT`
- `TRANSPORTS_TO`

## Current implementation boundary

`graph/MarketGraph.scala` creates a small GraphX graph with farmer, FPO, market, and buyer vertices. It is a source boundary and requires a Spark/Scala build configuration before execution.

## Future analyses

- Centrality of buyers, markets, and FPOs
- Community detection among supply participants
- Shortest paths for logistics planning
- Repeated transaction relationships
- Market accessibility and dependency analysis
- Buyer reliability based on completed transaction edges

Graph outputs should be treated as analytical evidence, not as a replacement for verification or contractual checks.
