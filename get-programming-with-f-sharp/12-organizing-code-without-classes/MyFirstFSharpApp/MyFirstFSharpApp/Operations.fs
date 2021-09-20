module MyFirstFSharpApp.Operations

open MyFirstFSharpApp.Domain

let getInitials customer = $"{customer.FirstName.[0]}.{customer.LastName.[0]}."
let isOlderThan age customer = customer.Age > age
