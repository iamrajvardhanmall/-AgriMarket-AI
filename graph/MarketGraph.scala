import org.apache.spark.SparkContext
import org.apache.spark.graphx.{Edge, Graph}
import org.apache.spark.rdd.RDD

object MarketGraph {
  def build(sparkContext: SparkContext): Graph[String, String] = {
    val vertices: RDD[(Long, String)] = sparkContext.parallelize(
      Seq((1L, "Farmer"), (2L, "FPO"), (3L, "Market"), (4L, "Buyer"))
    )
    val edges = sparkContext.parallelize(Seq(
      Edge(1L, 2L, "AGGREGATES"),
      Edge(2L, 3L, "SUPPLIES_TO"),
      Edge(3L, 4L, "SELLS_TO")
    ))
    Graph(vertices, edges)
  }
}
