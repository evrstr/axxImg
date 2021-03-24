import { VercelRequest, VercelResponse } from '@vercel/node'

export default function (req: VercelRequest, res: VercelResponse) {
    console.log(process.env.testEnv)
    const { name = 'World' } = req.query
    res.send(`Hello ${name}!`)
}