import {getQuoteQuery, getTickQuery} from '../queries';

const fetch = require('node-fetch');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

var dateFormat = require('dateformat');
var fs = require('file-system');

/* fetchHours function || fetches quote from graphql endpoint
  args: (hour: <string>, symbol: <string>) */

export const fetchHours = async (hour, symbol) => {
  var variables = {
    hour: hour,
    symbol: symbol,
  };

  var query = getQuoteQuery;
  fs.mkdir('../files/' + hour.toString(), () => {
    console.log('created dir for hour' + hour.toString());
  });

  // create csv write file
  fs.writeFile('../files/' + hour.toString() + '/quotes.csv', 'hi', err => {
    if (err) {
      return console.log(err);
    }
    console.log('created write file');
  });

  await fetch('http://139.59.181.241:4000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query,
      variables,
    }),
  })
    .then(res => res.json())
    .then(body => {
      // create csv column labels
      var csvWriter = createCsvWriter({
        path: '../files/' + hour.toString() + '/quotes.csv',
        header: [
          {
            id: 'timestamp',
            title: 'timestamp',
          },
          {
            id: 'reformattedDate',
            title: 'reformattedDate',
          },
          {
            id: 'hour',
            title: 'hour',
          },
          {
            id: 'symbol',
            title: 'symbol',
          },
          {
            id: 'bidPrice',
            title: 'bidPrice',
          },
          {
            id: 'bidSize',
            title: 'bidSize',
          },
          {
            id: 'askPrice',
            title: 'askPrice',
          },
          {
            id: 'askSize',
            title: 'askSize',
          },
          {
            id: 'midPrice',
            title: 'midPrice',
          },
          {
            id: 'microPrice',
            title: 'microPrice',
          },
        ],
      });
      var fullRecs = [];

      // push each quote to array
      body.data.quote.map(res => {
        var midPrice = (res.askPrice + res.bidPrice) / 2;
        var microPrice =
          (res.askPrice * res.bidSize + res.askPrice * res.askSize) / (res.bidSize + res.askSize);
        var reformattedDate = dateFormat(res.datetime, 'yymmddHHMMssl');
        var records = {
          timestamp: res.timestamp,
          reformattedDate: reformattedDate,
          hour: hour,
          symbol: res.symbol,
          bidPrice: res.bidPrice.toString(),
          bidSize: res.bidSize.toString(),
          askPrice: res.askPrice.toString(),
          askSize: res.askSize.toString(),
          midPrice: midPrice.toString(),
          microPrice: microPrice.toString(),
        };
        fullRecs.push(records);
      });

      //write records to csv file
      csvWriter
        .writeRecords(fullRecs)
        .then(() => {
          console.log('wrote records');
        })
        .catch(err => console.log(err));
    })
    .catch(e => console.log(e));
};

export const fetchTicks = async (hour, symbol) => {
  var variables = {
    hour: hour,
    symbol: symbol,
  };
  var query = getTickQuery;

  fs.writeFile('../files/' + hour.toString() + '/ticks.csv', 'hi', err => {
    if (err) {
      return console.log(err);
    }
    console.log('created write file for ticks');
  });

  await fetch('http://139.59.181.241:4000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query,
      variables,
    }),
  })
    .then(res => res.json())
    .then(body => {
      var csvWriter2 = createCsvWriter({
        path: '../files/' + hour.toString() + '/ticks.csv',
        header: [
          {
            id: 'timestamp',
            title: 'timestamp',
          },
          {
            id: 'reformattedDate',
            title: 'reformattedDate',
          },
          {
            id: 'hour',
            title: 'hour',
          },
          {
            id: 'symbol',
            title: 'symbol',
          },
          {
            id: 'side',
            title: 'side',
          },
          {
            id: 'size',
            title: 'size',
          },
          {
            id: 'price',
            title: 'price',
          },
          {
            id: 'tickDirection',
            title: 'tickDirection',
          },
          {
            id: 'trdMatchID',
            title: 'trdMatchID',
          },
          {
            id: 'volTime',
            title: 'volTime',
          },
          {
            id: 'tickTime',
            title: 'tickTime',
          },
        ],
      });
      var fullRecs = [];
      var volTime = 0;
      var tickTime = 0;

      body.data.tick.map(res => {
        volTime += res.size;
        tickTime += 1;
        var midPrice = (res.askPrice + res.bidPrice) / 2;
        var microPrice =
          (res.askPrice * res.bidSize + res.askPrice * res.askSize) / (res.bidSize + res.askSize);
        var reformattedDate = dateFormat(res.datetime, 'yymmddHHMMssl');
        var records = {
          timestamp: res.timestamp,
          reformattedDate: reformattedDate,
          hour: hour,
          symbol: res.symbol,
          side: res.side,
          size: res.size.toString(),
          price: res.price.toString(),
          tickDirection: res.tickDirection,
          trdMatchID: res.trdMatchID,
          volTime: volTime.toString(),
          tickTime: tickTime.toString(),
        };
        fullRecs.push(records);
      });

      csvWriter2
        .writeRecords(fullRecs)
        .then(() => {
          console.log('wrote tick records');
        })
        .catch(err => console.log(err));
    })
    .catch(e => console.log(e));
};
