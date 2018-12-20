export const getQuoteQuery = `
      query quote($hour: String!, $symbol: String!){
        quote(hour:$hour, symbol: $symbol){
            id
            timestamp
            symbol
            bidPrice
            bidSize
            askPrice
            askSize
        }
    }
`

export const getTickQuery = `
      query tick($hour: String!, $symbol: String!){
        tick(hour:$hour, symbol: $symbol){
            id
            timestamp
            hour
            symbol
            side
            size
            price
            tickDirection
            trdMatchID
        }
    }
`
