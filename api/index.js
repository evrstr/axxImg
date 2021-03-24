
module.exports = (req, res) => {
    console.log(process.env.testEnv)
    res.send(process.env.testEnv)
}