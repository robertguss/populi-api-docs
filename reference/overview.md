# Populi API2: overview

> A local copy of Populi's API2 reference (https://populi.co/api/), rebuilt for agents by `populi-docs`. Do not edit by hand; run `populi-docs sync` to refresh. Docs version: 2026-09-21 11:05:10 PST. Source: https://populi.co/api/

## Introduction

Welcome to the documentation site for the Populi API version 2.x.

This is a modern REST API, allowing you to integrate most of the data in your school's Populi instance with other outside services and your own custom software. The data object format shown here is also used by webhooks coming from Populi.

If you are looking for our [old API](https://support.populiweb.com/hc/en-us/articles/223798787-API-Basics), it is deprecated and will receive no further development (except for security updates), however you can still look up the [legacy API reference](https://support.populiweb.com/hc/en-us/articles/223798747-API-Reference).

If you need help, first check your API logs in Populi and look at the provided examples. The API channel on our Discord server is also a good place to ask for help or see what other developers are doing. For specific questions, please email [support@populi.co](mailto:support@populi.co).

> **Note:** This documentation updated on 2026-09-21 11:05:10 PST

## Authentication

> Every request must contain an API Key token in the header.

```shell
# With shell, you can just pass the correct header with each request
curl "https://yourschool.populiweb.com/api2/object/method" \
  -H "Authorization: Bearer YOUR_POPULI_API_KEY"
```

> Make sure to replace `YOUR_POPULI_API_KEY` with your API key token.

Populi uses API Keys to control access to the API. Populi Account Administrators can create API Keys and give them to developers to use. API Keys are given roles just like users are, which determines what exactly they have access to. You can also specify which users are Log Viewers of a particular key. You should make your developers log viewers of the keys they use so they can debug their own calls. To manage your API Keys, go to Account & Settings; under the Account heading, click API and go to the Keys view.

API Keys can have up to two active tokens associated with them. Tokens will look something like: `sk_j4U265CpkDEIXSAYwAVV1ryf2hiYo`

Populi expects for an API Key token to be included in all API requests to the server in a header that looks like the following:

`Authorization: Bearer sk_j4U265CpkDEIXSAYwAVV1ryf2hiYo`

> **Note:** You must replace `YOUR_POPULI_API_KEY` with your own API Key token in the provided code examples.

If you have a sandbox copy of your Populi instance that you use for testing, live API keys will not function on it. You will need to use `sk_sandbox_` prefixed keys instead. The opposite is also true. Sandbox keys will not work on the live site.

## Request and Response Format

All API calls will be to your school's Populi instance URL + `/api2/` + the route.

> Example

```plaintext
GET https://yourschool.populiweb.com/api2/people
```

Some API calls include parameters (integers) in the URL path.

> Example

```plaintext
POST https://yourschool.populiweb.com/api2/people/55782/phonenumbers/223950/update
```

Some calls require additional parameters. These will need to be included as JSON in the body of the request.

> Example

```plaintext
POST https://yourschool.populiweb.com/api2/people/55782/phonenumbers/create
{
  "number": "555-893-0032",
  "type": "home"
}
```

Most parameters correspond to properties of the data object in question and should be at the top level of your JSON request. However, some calls also have "action parameters", that should be nested under a key named `actions`.

> Example

```plaintext
POST https://yourschool.populiweb.com/api2/users/55782
{
  "username": "jimmy57",
  "actions": {
    "send_welcome_email": true
  }
}
```

All API calls will contain JSON in the body of the HTTP response. This response will always be either:

- A single data object
- A list object containing an array of data objects
- An error object containing information on what went wrong or why the request was invalid

There are a tiny handful of exceptions to this convention.

- API calls that contain a file upload will contain the file data in the body of the request and any additional parameters must be included as POST variables instead of JSON in the body.
- API calls that return a file to download (such as a XLS, CSV, or PDF), will contain the file in the response instead of JSON.
- If you are using a strict software library that does not allow GET calls to have any data in the request body, then you may alternately include parameters as JSON in the URL string. Use a single parameter in the url called `parameters` for this purpose.

> Alternate Example, JSON in a URL parameter

```plaintext
POST https://yourschool.populiweb.com/api2/courseofferings?parameters={"academic_term_id":5557}
```

JSON in the request must be valid. Trailing commas are not permitted. The documentation provides example requests and responses for every call.

All responses include the `"sandbox"` property. This will be set to `true` for responses or webhooks originating from a validation or demo instance. It will be `false` for data or events from your live production instance.

## Objects

Most API calls return a data object. A data object will always include its type name (e.g. `"object": "person"`) and its unique numeric id (e.g. `"id": "88932"` ). The data object will also contain many other fields, some of which may contain additional nested objects.

## Expandable Objects

> Example

```plaintext
GET https://yourschool.populiweb.com/api2/academicterms/994/courseofferings
{
    "expand": [
      "faculty",
      "grades"
    ]
}
```

Some calls are expandable. That means, in the request, you can specify that you want additional information included in the response. For example calling `/people/123` will give you back basic information about the person with ID 123. However, calling `/people/123` with `"expand": ["addresses", "phone_numbers", "tags"]` in the JSON request body will cause that person's addresses, phone numbers, and tags to be included in the response.

## Lists and Paging

> Example

```plaintext
GET https://yourschool.populiweb.com/api2/users
{
    "page": 2
}
```

Some API calls return a list of many data objects. For example, a call to find everyone with the last name `smith` may return several hundred results. Most lists contain a maximum of 200 records per response. You can use the `page` parameter in your request to request additional results. You can use the `limit` parameter in your request to reduce the maximum number of records returned per response.

Do not just add (e.g. `&page=2`) to the URL. The `page` parameter must be included in the JSON body of the request, like all parameters.

## Filter conditions for reports

> Example

```plaintext
GET https://yourschool.populiweb.com/api2/people
{
    "filter": {
        "0": {
            "logic": "ALL",
            "fields": [
                {
                    "name": "role",
                    "value": {
                        "id": "5",
                        "status": "ACTIVE"
                    },
                    "positive": "1"
                },
                {
                    "name": "tag",
                    "value": {
                        "display_text": "Summer Intensive",
                        "id": "443936"
                    },
                    "positive": "1"
                },
                {
                    "name": "citizenship",
                    "value": "US",
                    "positive": "0"
                }
            ]
        }
    }
}
```

The Populi interface provides many reports and index pages that allow you to construct complex filter conditions. For example, in the People report, you could construct conditions that effectively say "Show me all the active students with the tag 'Summer Intensive' who are not US citizens." All of these filter conditions are also available when making equivalent calls via the API. However, the format to specify these conditions is complex and requires a lot of nested properties. Instead of trying to explain how to build them, there is a much easier way:

- In Populi, navigate to the report that returns the data you care about.
- Use the interface to add a variety of conditions and logic until you get the results you want.
- Save the current state of the report as a preset and give it a name.
- Edit the preset report. In the dialog you will see a link titled "Show JSON for API".
- Copy and paste the filter condition JSON into your API code to get back the same results.

## Errors

> Example

```plaintext
{
  "object": "error",
  "code": 400,
  "type": "missing_parameter",
  "message": "Missing required parameter: academic_term_id",
  "sandbox": true
}
```

Some API calls will return an error object. The error object will contain additional details about what happened to assist with your debugging. Errors can result from many things such as requesting an object that doesn't exist, or supplying an invalid parameter, or trying to call a route your API key does not have permission to use.

## Rate Limits

Populi enforces API rate-limits in order to stay responsive for all users. The rate limits are as follows:

- 3AM - 7PM (Pacific Standard Time): 50 requests per minute per API key.
- 7PM - 3AM (Pacific Standard Time): 100 requests per minute per API key.
- Certain "heavy" API calls, cannot be called concurrently. That is, you can only make one heavy call at a time (e.g. pulling a Data Slicer report).
- There are additional per-IP and per-school limits.

If you pass your limit, Populi will return HTTP response code 429 (Too Many Requests).

### Handling 429 response codes by exponentially backing off

If your app exceeds its rate limit, you should pause for just over a minute before sending additional requests (that way you'll be guaranteed that the timer has been re-set). However, it's much more efficient to design your app to stay below the limit and avoid 429 responses altogether! You could do this by placing a small delay between calls.

If your app is making API requests from multiple threads, you'll need to make sure all threads are backing off when receiving 429 responses.

### Best practices to avoid rate limits

We recommend the following practices to reduce interruptions:

- Avoid constant polling. Listen for automation webhooks where possible.
- Add a small delay between rapid API calls (e.g. `sleep(1)` or equivalent)
- Cache your own data when you need to store specialized values or rapidly query large data sets.
- Only pull the data you need by adding filter condition parameters to reports

## Example Code

Example code for each call is provided below for each route in shell (curl), Ruby, Python, C#.Net, and PHP. Some of the provided examples depend on popular libraries you may need to include in your project. Feel free to use whatever libraries or methods you want.

If you a power user, but lacking in development skills, parts of this API can be accessed via the [Zapier](https://zapier.com) service for building third party integrations. If you are a Zapier user, you may email [support@populi.co](mailto:support@populi.co) and ask for a feature invite link.

If you are just getting started, we recommend making a few of your first calls using the [Postman](https://www.postman.com/downloads/) tool. Postman is a cross-platform API experimentation tool that provides an easy interface to see what is going on. We also have a Postman [collection of example calls](https://populi.co/api/images/populi.postman_collection.json) to get you started! After downloading it, go to the variable settings and replace the `school_url` with the URL of your own school's Populi instance. Under the Authorization settings you'll need to paste in a working API key of your own.
