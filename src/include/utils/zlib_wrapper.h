/*-------------------------------------------------------------------------
 *
 * zlib_wrapper.h
 *	 Wrapper functions for zlib to provide better integration with GPDB
 *
 * Copyright 2016 Pivotal Software, Inc.
 *
 *-------------------------------------------------------------------------
 */

#ifndef _UTILS___ZLIB_WRAPPER_H_
#define _UTILS___ZLIB_WRAPPER_H_

#include <zlib.h>

extern int gp_uncompress(Bytef *dest, uLongf *destLen, const Bytef *source, uLong sourceLen);
extern unsigned long gp_compressBound(unsigned long sourceLen);
extern int gp_compress2(Bytef *dest, uLongf *destLen, const Bytef *source, uLong sourceLen, int level);
extern gzFile gp_gzdopen(int fd, const char *mode);
extern int gp_gzclose (gzFile file);

#endif /* _UTILS___ZLIB_WRAPPER_H_ */
