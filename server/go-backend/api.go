package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func api() {
	router := gin.Default()
	router.GET("/", func(context *gin.Context) {
		context.JSON(http.StatusOK, gin.H{
			"message": "Hello world!",
		})
	})
	router.Run("localhost:5000")
}
