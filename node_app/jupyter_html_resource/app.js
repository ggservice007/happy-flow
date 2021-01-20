import Koa from 'koa';
import logger from 'koa-logger';
import Router from 'koa-router';
import koaBody from 'koa-bodyparser';
import helmet from 'koa-helmet';
import compress from 'koa-compress';
import convert from 'koa-convert';
import serve from 'koa-static';
import cors from 'kcors';
import fs from 'fs';
import path from 'path';
import os from 'os';
import _ from 'lodash';

const app = new Koa();
const router = new Router();
const PORT = 7071;


app.use(cors());
app.use(logger());
app.use(koaBody({
  jsonLimit: '2048mb',
  formLimit: '2048mb',
  textLimit: '2048mb'
}));
app.use(helmet());
app.use(compress());

app.use(serve(path.join(__dirname, './public/resource')));


app.use(serve('/happy_data/happy_jupyter/8000_0101_happy_flow/happy-flow'));


router.all('/', async (ctx, next) => {
    ctx.body = {
      "version": "1.0.0",
      "description": "Jupyter Html Resource Server"
    };
});

app.use(router.routes());
app.use(router.allowedMethods());


app.listen(PORT, '0.0.0.0' ,() => {
  console.log(`Server is now running on http://localhost:${PORT}`)
});

app.timeout = 60 * 60 * 1000;
