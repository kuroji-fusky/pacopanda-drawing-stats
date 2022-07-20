BINARY_NAME=pacopanda-drawing-api

build:
	GOARCH=amd64 GOOS=linux go build -o ${BINARY_NAME}-linux api.go
	GOARCH=amd64 GOOS=window go build -o ${BINARY_NAME}-window api.go

run:
	./${BINARY_NAME}

tidy:
	go tidy

run-api:
	go run . -a

run-scraper:
	go run . -s

clean:
	go clean
	rm ${BINARY_NAME}-linux
	rm ${BINARY_NAME}-windows