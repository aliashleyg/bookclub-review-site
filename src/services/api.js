const API_URL = 'http://127.0.0.1:8000'

export async function getBooks() {
    const res = await fetch(`${API_URL}/books`)
    return res.json()
}