import { getQuoteQuery, getTickQuery } from './queries';
const fetch = require('node-fetch');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

var dateFormat = require('dateformat');
var fs = require('file-system');

// var hour = "18121403";
var hour = process.argv[2];
var symbol = process.argv[3];

const fetchHours = (hour, symbol) => {

    const variables = {
        hour: hour,
        symbol: symbol
    }
    var query = getQuoteQuery;
    fs.mkdir('files/' + hour.toString(), () => {
        console.log('created dir for hour' + hour.toString())
    })
    fs.writeFile('files/' + hour.toString() + '/quotes.csv', "hi", (err) => {
        if (err) {
            return console.log(err);
        }
        console.log('created write file')
    })

    fetch("http://139.59.181.241:4000/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query, variables })
    })
        .then((res) => res.json())
        .then(body => {




            const csvWriter = createCsvWriter({
                path: 'files/' + hour.toString() + '/quotes.csv',
                header: [
                    { id: 'timestamp', title: 'timestamp' },
                    { id: 'reformattedDate', title: 'reformattedDate' },
                    { id: 'hour', title: 'hour' },
                    { id: 'symbol', title: 'symbol' },
                    { id: 'bidPrice', title: 'bidPrice' },
                    { id: 'bidSize', title: 'bidSize' },
                    { id: 'askPrice', title: 'askPrice' },
                    { id: 'askSize', title: 'askSize' },
                    { id: 'midPrice', title: 'midPrice' },
                    { id: 'microPrice', title: 'microPrice' }
                ]
            })
            var fullRecs = [];

            body.data.quote.map((res) => {


                var midPrice = (res.askPrice + res.bidPrice) / 2
                var microPrice = (((res.askPrice * res.bidSize) + (res.askPrice * res.askSize)) / (res.bidSize + res.askSize))
                var reformattedDate = dateFormat(res.datetime, "yymmddHHMMssl")
                var records = {
                    timestamp: res.timestamp, reformattedDate: reformattedDate, hour: hour, symbol: res.symbol, bidPrice: res.bidPrice.toString(), bidSize: res.bidSize.toString(),
                    askPrice: res.askPrice.toString(), askSize: res.askSize.toString(), midPrice: midPrice.toString(), microPrice: microPrice.toString()
                }
                fullRecs.push(records)

            })

            csvWriter.writeRecords(fullRecs)
                .then(() => {
                    console.log('wrote records')
                })
                .catch((err) => console.log(err))



        })
        .catch((e) => console.log(e));


}
const fetchTicks = (hour, symbol) => {

    const variables = {
        hour: hour,
        symbol: symbol
    }
    var query = getTickQuery;

    fs.writeFile('files/' + hour.toString() + '/ticks.csv', "hi", (err) => {
        if (err) {
            return console.log(err);
        }
        console.log('created write file for ticks')
    })

    fetch("http://139.59.181.241:4000/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query, variables })
    })
        .then((res) => res.json())
        .then(body => {

            const csvWriter = createCsvWriter({
                path: 'files/' + hour.toString() + '/quotes.csv',
                header: [
                    { id: 'timestamp', title: 'timestamp' },
                    { id: 'reformattedDate', title: 'reformattedDate' },
                    { id: 'hour', title: 'hour' },
                    { id: 'symbol', title: 'symbol' },
                    { id: 'side', title: 'side' },
                    { id: 'size', title: 'size' },
                    { id: 'tickDirection', title: 'tickDirection' },
                    { id: 'trdMatchID', title: 'trdMatchID' },
                    { id: 'volTime', title: 'accVolTime' },
                    { id: 'tickTime', title: 'tickTime' }
                ]
            })
            var fullRecs = [];
            var volTime = 0;
            var tickTime = 0;

            body.data.quote.map((res) => {

                accVolTime += res.size;
                var midPrice = (res.askPrice + res.bidPrice) / 2
                var microPrice = (((res.askPrice * res.bidSize) + (res.askPrice * res.askSize)) / (res.bidSize + res.askSize))
                var reformattedDate = dateFormat(res.datetime, "yymmddHHMMssl")
                var records = {
                    timestamp: res.timestamp, reformattedDate: reformattedDate, hour: hour, symbol: res.symbol, bidPrice: res.bidPrice.toString(), bidSize: res.bidSize.toString(),
                    askPrice: res.askPrice.toString(), askSize: res.askSize.toString(), midPrice: midPrice.toString(), microPrice: microPrice.toString()
                }
                fullRecs.push(records)

            })

            csvWriter.writeRecords(fullRecs)
                .then(() => {
                    console.log('wrote records')
                })
                .catch((err) => console.log(err))



        })
        .catch((e) => console.log(e));


}


fetchHours(hour, symbol)

setTimeout(1000, () => {
    fetchTicks(hour, symbol)
})