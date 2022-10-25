const { application } = require('express');
const express = require('express');
const app = express();
const port = 3050;

app.get('/', (req, res) => {
    res.send('The backend is running');
});

app.listen(port, () => {
    console.log(`Backend is running on port ${port}`);
});
