package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"os"
)

func Healthcheck(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"status": "ok"})
}

func main() {
	fmt.Println("hello")

	router := gin.Default()

	router.GET("/healthcheck", Healthcheck)

	backendPort := os.Getenv("BACKEND_PORT")

	fmt.Printf("Running on port: %s\n", backendPort)

	router.Run(fmt.Sprintf(":%s", backendPort))
}
