const express = require("express")
const app = express()
const PORT = 5030

app.get('/', (req, res) => {
    res.send ('Student Name: Eslam Gamal Gameel El-Elelamy <br\> <br\> Student Section: section 1')
})

app.listen(PORT, () => {
    console.log('Example app listening at http://localhost:5030')
})