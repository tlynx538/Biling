package main

import (
	"fmt"
	"biling/controllers"
	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Printf("Biling API v 0.1\n")
	router := gin.Default()
	//define routes here
	router.GET("/", controllers.Home)
	router.POST("/create", controllers.CreateBill)
	router.GET("/show",controllers.ShowBill)
	router.Run("localhost:8080")
}
