module.exports = (req, res) => {

    res.status(200).send(toString(req))
}