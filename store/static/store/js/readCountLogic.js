async function readCount(pk) {
    const url = `${pk}/`
    try {
        const response = await fetch(url)
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`)
        }
    } catch (error) {
        console.error(`Read count update error: ${error.message}`)
    }

}