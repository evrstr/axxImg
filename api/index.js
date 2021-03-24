module.exports = (req, res) => {
    console.log(process.env.testEnv)
    res.status(200).send(toString(process.env.testEnv))
}