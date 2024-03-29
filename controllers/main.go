package controllers

import (
	"net/http"
	"github.com/lithammer/shortuuid"
	"github.com/gin-gonic/gin"
)

type BillItem struct {
	SlNo 	int 	`json:"sl_no"`
	Desc 	string 	`json:"desc"`
	Qty 	int 	`json:"qty"`
	Price 	float64 `json:"price"`
}

type AddBill struct {
	Items [] 	BillItem 	`json:"items"`
	TotalPrice 	float64 	`json:"total_price"`
	StatusId 	int			`json:"status_id"`
}

type Bill struct {
	Billid 		string 		`json:"bill_id"`
	Items 		[]BillItem 	`json:"items"`
	TotalPrice 	float64 	`json:"total_price"`
	StatusId 	int 		`json:"status_id"`
}

func Home(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"message": "Welcome to Billing API!"})
}

func CreateBill(c *gin.Context) {
	// generate bill_id
	bill_id := shortuuid.New()
	// validate bill
	var inputBill AddBill
	var billItem[] BillItem
	var grand_total float64 = 0


	if err := c.BindJSON(&inputBill); err!= nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	for _,i := range inputBill.Items {
		grand_total += (i.Price * float64(i.Qty))
		billItem = append(billItem,i)
	}
	// bill preparation
	var finalBill = Bill{bill_id,billItem,inputBill.TotalPrice,inputBill.StatusId}
	if(inputBill.TotalPrice == grand_total) {
		c.IndentedJSON(http.StatusOK, finalBill)
	} else {
		c.IndentedJSON(http.StatusNotAcceptable, gin.H{"error":"Discrepancy in Totalling."})
	}
}

func ShowBill(c *gin.Context){
	return
}

func DeleteBill(c *gin.Context){
	return
}
