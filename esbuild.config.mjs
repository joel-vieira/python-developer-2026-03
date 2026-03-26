import esbuild from 'esbuild';
import { sassPlugin } from 'esbuild-sass-plugin';

const watch = process.argv.includes('--watch');

const config = {
  entryPoints: ['static/src/main.scss'],
  outdir: 'static/dist',
  bundle: true,
  minify: process.env.NODE_ENV === 'production',
  plugins: [
    sassPlugin(),
    {
      name: 'rebuild-log',
      setup(build) {
        build.onEnd((result) => {
          const time = new Date().toLocaleTimeString();
          if (result.errors.length) {
            console.log(`[${time}] Build failed`);
          } else {
            console.log(`[${time}] Build complete`);
          }
        });
      },
    },
  ],
};
if (watch) {
  const context = await esbuild.context(config);
  await context.watch();
  console.log('Watching for changes...');
} else {
  await esbuild.build(config);
}
