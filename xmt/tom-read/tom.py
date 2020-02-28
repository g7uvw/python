import cstruct
from PIL import Image
import numpy as np

class TOMHEAD(cstruct.CStruct):
	__byte_order__ = cstruct.LITTLE_ENDIAN
	__struct__ = """

	uint16_t xsize;
	uint16_t ysize;
	uint16_t zsize;
	uint16_t lmarg;
	uint16_t rmarg;
	uint16_t tmarg;
	uint16_t bmarg;
	uint16_t tzmarg;
	uint16_t bzmarg;
	uint16_t num_samples;
	uint16_t num_proj;
	uint16_t num_blocks;
	uint16_t num_slices;
	uint16_t bin;
	uint16_t gain;
	uint16_t speed;
	uint16_t pepper;
	uint16_t issue;
	uint16_t num_frames;
	uint16_t spare_int[13];
    
	float scale;
	float offset;
	float voltage;
	float current;
	float thickness;
	float pixel_size;
	float distance;
	float exposure;
    float mag_factor;
	float filterb;
	float correction_factor;
	float spare_float[2];
    
	uint32_t z_shift;
	uint32_t z;
	uint32_t theta;
    
	char time[26];
	char duration[12];
	char owner[21];
	char user[5];
	char specimen[32];
	char scan[32];
	char comment[64];
	char spare_char[192];
	"""
	def print_info(self):
		print("X: %s" % self.xsize)
		print("Y: %s" % self.ysize)
		print("Z: %s" % self.zsize)
		#print("Owner: %s" % self.owner)

tomfile = "as_tooth1_scan3.tom"
with open(tomfile, "rb") as f:
    tom = TOMHEAD();
    header = f.read(len(tom));
    tom.unpack(header)
    tom.print_info();
    total = tom.xsize*tom.ysize*tom.zsize;
    print ("Tota data size (bytes): %s" % total);
    f.seek(len(tom));
    volume = np.fromfile(f, dtype='uint8',count=tom.xsize*tom.ysize)
    #f.read(tom.xsize*tom.ysize*tom.zsize);
    wibble = volume.shape;
    volume.reshape(tom.xsize,tom.ysize)
    wibble2 = volume.shape;
img = Image.fromarray(volume, 'L')
img.show()









