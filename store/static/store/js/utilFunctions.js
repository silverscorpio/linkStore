function getCookie(name) {
    // from django docs - gets the csrf token from the cookies
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getPostData(val) {
    // returns the data to be sent with the POST request for updating the read and marked statuses
    const vals = val.split("_")
    const field = vals[0]
    const field_pk = vals[1]

    const csrftoken = getCookie('csrftoken');
    let checkbox = document.querySelector(`input[name=${val}]`)
    let queryParams = new URLSearchParams()
    queryParams.append("field", field)
    queryParams.append("status", (checkbox.checked ? 1 : 0).toString())

    let url = `${field_pk}/`

    return [url,
        {
            method: "POST",
            headers: {'X-CSRFToken': csrftoken},
            body: queryParams,
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
    ]
}

function updateCheckboxBackend(val) {
    // ability to manually mark the read status and marked status to true and false using checkbox
    const postData = getPostData(val)
    fetch(postData[0], postData[1])
        .then(response => {
            if (response.status === 200) {
                console.log(`Updated: ${postData[1].body.get("field")} status`)
            }
        })
        .catch(error => {
            console.error(`Failed: ${postData[1].body.get("field")} status ${error}`)
        })

}

function readCountAndStatusUpdate(pk) {
    // opening the url triggers an update on the read count and read status
    const url = `${pk}/`
    const csrftoken = getCookie('csrftoken');
    let queryParams = new URLSearchParams()
    queryParams.append("field", "read_count")
    queryParams.append("status", `${pk}`)
    const data = {
        method: "POST",
        headers: {'X-CSRFToken': csrftoken},
        body: queryParams,
        mode: 'same-origin'
    }

    fetch(url, data)
        .then(response => {
            if (response.status === 200) {
                console.log(`Updated: ${data.body.get("field")}`)
            }
        })
        .catch(error => {
            console.error(`Failed: ${data.body.get("field")} ${error}`)
        })
}